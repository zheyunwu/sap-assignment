import {
    CreateParams,
    DataProvider,
    fetchUtils
} from "react-admin";
import { stringify } from "query-string";

const apiUrl = "http://localhost:8000";
const httpClient = fetchUtils.fetchJson;

type PostParams = {
    tag_name: string;
    dockerfile: {
        rawFile: File;
        src?: string;
        title?: string;
    };
};

const createPostFormData = (params: CreateParams<PostParams>) => {
    const formData = new FormData();
    params.data.dockerfile?.rawFile && formData.append("dockerfile", params.data.dockerfile.rawFile);
    params.data.tag_name && formData.append("tag_name", params.data.tag_name);

    return formData;
};

export const dataProvider: DataProvider = {
    getList: (resource, params) => {
        const { page, perPage } = params.pagination;
        const { field, order } = params.sort;
        const query = {
            sort: JSON.stringify([field, order]),
            range: JSON.stringify([(page - 1) * perPage, page * perPage - 1]),
            filter: JSON.stringify(params.filter),
        };
        const url = `${apiUrl}/${resource}?${stringify(query)}`;

        return httpClient(url).then(({ headers, json }) => ({
            data: json.items,
            total: json.total
        }));
    },

    // getOne: (resource, params) => {
    //     return httpClient(`${apiUrl}/${resource}/${params.id}`).then(({ json }) => ({
    //         data: json,
    //     }))
    // },

    create: (resource, params) => {
        if (resource === "images") {
            const formData = createPostFormData(params);
            return fetchUtils
                .fetchJson(`${apiUrl}/${resource}`, {
                    method: "POST",
                    body: formData,
                })
                .then(({ json }) => ({ data: json }));
        }

        return httpClient(`${apiUrl}/${resource}`, {
            method: 'POST',
            body: JSON.stringify(params.data),
        }).then(({ json }) => ({
            data: { ...params.data, id: json.id },
        }))
    }
}
